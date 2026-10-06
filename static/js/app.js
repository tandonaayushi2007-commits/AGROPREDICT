/**
 * AgroPredict - Frontend Application Logic
 * 
 * Features:
 * - Real-time and submission input validation
 * - Asynchronous AJAX communication with Flask backend POST /predict
 * - Interactive prediction result & crop agronomic profile rendering
 * - Prediction history persistence via browser localStorage
 * - Quick presets for instant testing
 * - Form reset & history management
 */

// Local storage key for persisting prediction history
const STORAGE_KEY = 'agropredict_history_v1';

// Validation constraints matching agronomic realistic boundaries
const FIELD_CONSTRAINTS = {
    N: { min: 0, max: 140, label: 'Nitrogen (N)', unit: 'kg/ha' },
    P: { min: 5, max: 145, label: 'Phosphorus (P)', unit: 'kg/ha' },
    K: { min: 5, max: 205, label: 'Potassium (K)', unit: 'kg/ha' },
    temperature: { min: 8.0, max: 45.0, label: 'Temperature', unit: '°C' },
    humidity: { min: 10.0, max: 100.0, label: 'Relative Humidity', unit: '%' },
    ph: { min: 3.5, max: 10.0, label: 'Soil pH', unit: '' },
    rainfall: { min: 20.0, max: 300.0, label: 'Rainfall', unit: 'mm' }
};

// Built-in presets for quick demonstration
const PRESETS = {
    rice: { N: 90, P: 42, K: 43, temperature: 21.5, humidity: 82.0, ph: 6.5, rainfall: 210.0 },
    coffee: { N: 101, P: 29, K: 32, temperature: 26.5, humidity: 58.0, ph: 6.8, rainfall: 160.0 },
    cotton: { N: 118, P: 47, K: 20, temperature: 24.0, humidity: 80.0, ph: 6.9, rainfall: 80.0 },
    apple: { N: 24, P: 134, K: 198, temperature: 22.0, humidity: 92.5, ph: 6.1, rainfall: 110.0 },
    watermelon: { N: 99, P: 18, K: 51, temperature: 25.5, humidity: 88.0, ph: 6.5, rainfall: 50.0 }
};

// DOM Elements
const form = document.getElementById('predictionForm');
const btnPredict = document.getElementById('btnPredict');
const btnReset = document.getElementById('btnReset');
const predictSpinner = document.getElementById('predictSpinner');
const formAlert = document.getElementById('formAlert');
const alertMessage = document.getElementById('alertMessage');

// Result View Elements
const resultPlaceholder = document.getElementById('resultPlaceholder');
const predictionContent = document.getElementById('predictionContent');
const cropAvatar = document.getElementById('cropAvatar');
const cropTitle = document.getElementById('cropTitle');
const cropScientific = document.getElementById('cropScientific');
const confidenceValue = document.getElementById('confidenceValue');
const cropCategory = document.getElementById('cropCategory');
const cropDescription = document.getElementById('cropDescription');
const specSoil = document.getElementById('specSoil');
const specTemp = document.getElementById('specTemp');
const specWater = document.getElementById('specWater');
const specSeason = document.getElementById('specSeason');
const farmingTipsList = document.getElementById('farmingTipsList');
const cropMarketValue = document.getElementById('cropMarketValue');
const alternativesList = document.getElementById('alternativesList');

// History View Elements
const historyEmpty = document.getElementById('historyEmpty');
const historyTable = document.getElementById('historyTable');
const historyTbody = document.getElementById('historyTbody');
const historyCount = document.getElementById('historyCount');
const btnClearHistory = document.getElementById('btnClearHistory');


/**
 * Initializes application event listeners and loads saved history on startup.
 */
document.addEventListener('DOMContentLoaded', () => {
    // Form submission
    form.addEventListener('submit', handleFormSubmit);

    // Form reset
    btnReset.addEventListener('click', handleFormReset);

    // Clear history
    btnClearHistory.addEventListener('click', handleClearHistory);

    // Preset button click handlers
    document.querySelectorAll('.preset-chip').forEach(chip => {
        chip.addEventListener('click', (e) => {
            const presetKey = e.currentTarget.getAttribute('data-preset');
            applyPreset(presetKey);
        });
    });

    // Real-time input validation on change/blur
    Object.keys(FIELD_CONSTRAINTS).forEach(fieldId => {
        const inputElem = document.getElementById(`input-${fieldId}`);
        if (inputElem) {
            inputElem.addEventListener('input', () => clearFieldError(fieldId));
            inputElem.addEventListener('blur', () => validateSingleField(fieldId));
        }
    });

    // Render persisted history from localStorage
    renderHistory();
});


/**
 * Applies preset parameter values into the form fields.
 * 
 * @param {string} presetKey - The identifier of the preset
 */
function applyPreset(presetKey) {
    const data = PRESETS[presetKey];
    if (!data) return;

    hideAlert();
    clearAllFieldErrors();

    Object.keys(data).forEach(field => {
        const input = document.getElementById(`input-${field}`);
        if (input) {
            input.value = data[field];
            // Highlight briefly for user feedback
            input.style.backgroundColor = '#e8f5e9';
            setTimeout(() => { input.style.backgroundColor = ''; }, 400);
        }
    });
}


/**
 * Validates a single input field against defined constraints.
 * 
 * @param {string} fieldId - Name of the field (N, P, K, etc.)
 * @returns {boolean} True if field is valid, false otherwise.
 */
function validateSingleField(fieldId) {
    const inputElem = document.getElementById(`input-${fieldId}`);
    const wrapper = document.getElementById(`wrapper-${fieldId}`);
    const errorElem = document.getElementById(`error-${fieldId}`);
    const rule = FIELD_CONSTRAINTS[fieldId];

    if (!inputElem || !rule) return true;

    const rawVal = inputElem.value.trim();

    if (rawVal === '') {
        showFieldError(fieldId, `Please enter ${rule.label}`);
        return false;
    }

    const numVal = parseFloat(rawVal);
    if (isNaN(numVal)) {
        showFieldError(fieldId, `Must be a valid number`);
        return false;
    }

    if (numVal < rule.min || numVal > rule.max) {
        showFieldError(fieldId, `Range: ${rule.min} – ${rule.max} ${rule.unit}`);
        return false;
    }

    clearFieldError(fieldId);
    return true;
}


/**
 * Shows an inline validation error message for a specific input field.
 */
function showFieldError(fieldId, message) {
    const wrapper = document.getElementById(`wrapper-${fieldId}`);
    const errorElem = document.getElementById(`error-${fieldId}`);
    if (wrapper) wrapper.classList.add('has-error');
    if (errorElem) errorElem.textContent = message;
}


/**
 * Clears an inline validation error for a specific input field.
 */
function clearFieldError(fieldId) {
    const wrapper = document.getElementById(`wrapper-${fieldId}`);
    const errorElem = document.getElementById(`error-${fieldId}`);
    if (wrapper) wrapper.classList.remove('has-error');
    if (errorElem) errorElem.textContent = '';
}


/**
 * Clears all inline validation errors.
 */
function clearAllFieldErrors() {
    Object.keys(FIELD_CONSTRAINTS).forEach(fieldId => clearFieldError(fieldId));
}


/**
 * Displays a global alert banner above the form.
 */
function showAlert(message) {
    formAlert.classList.remove('hidden');
    alertMessage.textContent = message;
}


/**
 * Hides the global alert banner.
 */
function hideAlert() {
    formAlert.classList.add('hidden');
    alertMessage.textContent = '';
}


/**
 * Handles form submission: validates inputs and calls Flask POST /predict API.
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    hideAlert();

    // 1. Perform client-side validation on all 7 fields
    let isValid = true;
    const payload = {};

    Object.keys(FIELD_CONSTRAINTS).forEach(fieldId => {
        const fieldValid = validateSingleField(fieldId);
        if (!fieldValid) {
            isValid = false;
        } else {
            payload[fieldId] = parseFloat(document.getElementById(`input-${fieldId}`).value);
        }
    });

    if (!isValid) {
        showAlert('Please correct the highlighted field errors before submitting.');
        return;
    }

    // 2. Set button loading state
    setLoadingState(true);

    try {
        // 3. Make asynchronous POST request to Flask API
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        // 4. Handle backend validation or server errors
        if (!response.ok || result.status !== 'success') {
            if (result.errors) {
                // Display server-side field validation errors
                Object.keys(result.errors).forEach(key => {
                    showFieldError(key, result.errors[key]);
                });
                showAlert(result.message || 'Validation error from server.');
            } else {
                showAlert(result.message || 'Prediction failed. Please try again.');
            }
            return;
        }

        // 5. Render predicted crop and agronomic details
        displayPredictionResult(result);

        // 6. Persist successful prediction to localStorage history
        savePredictionToHistory(result, payload);

    } catch (networkError) {
        console.error('API Error:', networkError);
        showAlert('Could not communicate with the AgroPredict server. Please verify Flask backend is running.');
    } finally {
        setLoadingState(false);
    }
}


/**
 * Updates UI loading indicators during prediction.
 */
function setLoadingState(isLoading) {
    if (isLoading) {
        btnPredict.disabled = true;
        predictSpinner.classList.remove('hidden');
        btnPredict.querySelector('.btn-text').textContent = 'Analyzing Parameters...';
    } else {
        btnPredict.disabled = false;
        predictSpinner.classList.add('hidden');
        btnPredict.querySelector('.btn-text').textContent = 'Predict Recommended Crop';
    }
}


/**
 * Renders the returned prediction response into the result card.
 * 
 * @param {Object} data - API response payload from /predict
 */
function displayPredictionResult(data) {
    const info = data.crop_info || {};

    // Switch view from placeholder to active result
    resultPlaceholder.classList.add('hidden');
    predictionContent.classList.remove('hidden');

    // Populate Hero Details
    cropAvatar.textContent = info.icon || '🌱';
    cropTitle.textContent = info.name || data.predicted_crop.toUpperCase();
    cropScientific.textContent = info.scientific_name ? `(${info.scientific_name})` : '';
    confidenceValue.textContent = `${data.confidence || 99}%`;
    cropCategory.textContent = info.category || 'Agricultural Crop';
    cropDescription.textContent = info.description || '';

    // Populate Key Specs
    specSoil.textContent = info.soil_type || 'Fertile Loam';
    specTemp.textContent = info.ideal_temp || 'Local Climate';
    specWater.textContent = info.water_requirement || 'Moderate';
    specSeason.textContent = info.growing_season || 'Seasonal';

    // Populate Practical Agronomic Tips
    farmingTipsList.innerHTML = '';
    if (info.farming_tips && info.farming_tips.length > 0) {
        info.farming_tips.forEach(tip => {
            const li = document.createElement('li');
            li.textContent = tip;
            farmingTipsList.appendChild(li);
        });
    }

    // Populate Market / Economic Info
    cropMarketValue.textContent = info.economic_value || 'Strong commercial potential under standard practices.';

    // Populate Top 3 Alternative Candidates
    alternativesList.innerHTML = '';
    if (data.top_candidates && data.top_candidates.length > 0) {
        data.top_candidates.forEach(candidate => {
            const item = document.createElement('div');
            item.className = 'alt-item';
            item.innerHTML = `
                <div class="alt-name">
                    <span>${candidate.icon}</span>
                    <span>${candidate.display_name}</span>
                </div>
                <div class="alt-bar-bg">
                    <div class="alt-bar-fill" style="width: ${Math.max(candidate.probability, 3)}%;"></div>
                </div>
                <div class="alt-prob">${candidate.probability}%</div>
            `;
            alternativesList.appendChild(item);
        });
    }

    // Smooth scroll to result on mobile screens
    if (window.innerWidth <= 992) {
        document.getElementById('resultContainer').scrollIntoView({ behavior: 'smooth' });
    }
}


/**
 * Resets form fields, clears validation states, and restores the result placeholder.
 */
function handleFormReset() {
    form.reset();
    clearAllFieldErrors();
    hideAlert();

    // Reset result view to placeholder
    predictionContent.classList.add('hidden');
    resultPlaceholder.classList.remove('hidden');
}


// ============================================================================
// Prediction History Management (localStorage)
// ============================================================================

/**
 * Saves a completed prediction to localStorage.
 */
function savePredictionToHistory(apiResponse, inputData) {
    const history = getStoredHistory();
    const entry = {
        id: Date.now(),
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        crop: apiResponse.predicted_crop,
        displayName: apiResponse.display_name || apiResponse.predicted_crop,
        icon: apiResponse.icon || '🌱',
        confidence: apiResponse.confidence || 99,
        inputs: inputData
    };

    // Prepend new entry, keep up to 25 items
    history.unshift(entry);
    if (history.length > 25) {
        history.pop();
    }

    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
    renderHistory();
}


/**
 * Retrieves history list from localStorage safely.
 */
function getStoredHistory() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        return stored ? JSON.parse(stored) : [];
    } catch (e) {
        console.error('Failed reading history from localStorage:', e);
        return [];
    }
}


/**
 * Renders the prediction history table.
 */
function renderHistory() {
    const history = getStoredHistory();
    historyCount.textContent = `${history.length} ${history.length === 1 ? 'entry' : 'entries'}`;

    if (history.length === 0) {
        historyEmpty.classList.remove('hidden');
        historyTable.classList.add('hidden');
        return;
    }

    historyEmpty.classList.add('hidden');
    historyTable.classList.remove('hidden');
    historyTbody.innerHTML = '';

    history.forEach(item => {
        const tr = document.createElement('tr');
        const inp = item.inputs || {};

        tr.innerHTML = `
            <td><strong>${item.timestamp}</strong></td>
            <td>
                <span class="crop-badge-pill">
                    <span>${item.icon}</span>
                    <span>${item.displayName}</span>
                </span>
            </td>
            <td><strong style="color: var(--primary-700);">${item.confidence}%</strong></td>
            <td>
                <div class="param-chips-summary">
                    <span class="p-chip">N: ${inp.N}</span>
                    <span class="p-chip">P: ${inp.P}</span>
                    <span class="p-chip">K: ${inp.K}</span>
                    <span class="p-chip">T: ${inp.temperature}°C</span>
                    <span class="p-chip">H: ${inp.humidity}%</span>
                    <span class="p-chip">pH: ${inp.ph}</span>
                    <span class="p-chip">Rain: ${inp.rainfall}mm</span>
                </div>
            </td>
            <td>
                <button type="button" class="btn-history-load" title="Load these parameters into form">
                    Load
                </button>
            </td>
        `;

        // Click handler to load historic parameters back into form
        const loadBtn = tr.querySelector('.btn-history-load');
        loadBtn.addEventListener('click', () => {
            loadHistoryItemIntoForm(item.inputs);
        });

        historyTbody.appendChild(tr);
    });
}


/**
 * Loads values from a history entry back into the input fields.
 */
function loadHistoryItemIntoForm(inputs) {
    if (!inputs) return;
    hideAlert();
    clearAllFieldErrors();

    Object.keys(inputs).forEach(key => {
        const elem = document.getElementById(`input-${key}`);
        if (elem) {
            elem.value = inputs[key];
        }
    });

    // Scroll to predictor form
    document.getElementById('predictor').scrollIntoView({ behavior: 'smooth' });
}


/**
 * Clears prediction history from localStorage.
 */
function handleClearHistory() {
    const history = getStoredHistory();
    if (history.length === 0) return;

    if (confirm('Are you sure you want to clear your prediction history?')) {
        localStorage.removeItem(STORAGE_KEY);
        renderHistory();
    }
}
