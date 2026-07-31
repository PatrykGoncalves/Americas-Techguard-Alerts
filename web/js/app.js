/*********************************************************************
 * Americas TechGuard
 * Environmental Alert System
 *********************************************************************/

const PAYLOAD_PATH = "../outputs/latest_payload.json";

let lastTimestamp = null;


/*********************************************************************
 * Inicialização
 *********************************************************************/

window.onload = () => {

    updateClock();

    loadPayload();

    setInterval(updateClock, 1000);

    setInterval(loadPayload, 5000);

    document
        .getElementById("refresh-button")
        .addEventListener(
            "click",
            loadPayload
        );

};


/*********************************************************************
 * Carrega o payload
 *********************************************************************/

async function loadPayload() {

    try {

        const response =
            await fetch(
                PAYLOAD_PATH,
                {
                    cache: "no-store"
                }
            );

        if (!response.ok) {

            throw new Error("Payload not found.");

        }

        const payload =
            await response.json();

        if (payload.timestamp === lastTimestamp) {

            return;

        }

        lastTimestamp =
            payload.timestamp;

        updateInterface(payload);

    }

    catch (error) {

        console.error(error);

        showOffline();

    }

}


/*********************************************************************
 * Atualiza interface
 *********************************************************************/

function updateInterface(payload) {

    updateStatus(true);

    updateRisk(payload);

    updateSensor(payload);

    updateLocation(payload);

    updatePrediction(payload);

    updateRecommendation(payload)

    updateTimestamp(payload);

    configureMapButton(payload);

    animateCard();

}

/*********************************************************************
 * Prediction
 *********************************************************************/

function updatePrediction(payload) {

    document
        .getElementById("prediction")
        .textContent =
        payload.risk.prediction_horizon;

}

function updateRecommendation(payload) {

    document
        .getElementById("recommended-action")
        .textContent =
        payload.risk.recommended_action;

}

/*********************************************************************
 * Atualiza Status
 *********************************************************************/

function updateStatus(isOnline) {

    const indicator =
        document.getElementById("status-indicator");

    const text =
        document.getElementById("status-text");

    indicator.classList.remove(
        "online",
        "offline"
    );

    if (isOnline) {

        indicator.classList.add("online");

        text.textContent =
            "System Online";

    }

    else {

        indicator.classList.add("offline");

        text.textContent =
            "Offline";

    }

}


/*********************************************************************
 * Atualiza risco
 *********************************************************************/

function updateRisk(payload) {

    const badge =
        document.getElementById("risk-level");

    const message =
        document.getElementById("alert-message");

    badge.classList.remove(
        "safe",
        "attention",
        "alert",
        "critical"
    );

    let icon = "🟢";

    switch (payload.risk.risk_level) {

        case "SAFE":

            icon = "🟢";
            badge.classList.add("safe");
            break;

        case "ATTENTION":

            icon = "🟡";
            badge.classList.add("attention");
            break;

        case "ALERT":

            icon = "🟠";
            badge.classList.add("alert");
            break;

        case "CRITICAL":

            icon = "🔴";
            badge.classList.add("critical");
            break;

    }

    badge.textContent =
        icon + " " +
        payload.risk.risk_level;

    message.textContent =
        payload.risk.alert_message;

    if (
        payload.risk.risk_level === "ALERT"
        ||
        payload.risk.risk_level === "CRITICAL"
    ) {

        showNotification(
            payload.risk.alert_message
        );

    }

}


/*********************************************************************
 * Atualiza sensor
 *********************************************************************/

function updateSensor(payload) {

    document
        .getElementById("sensor-type")
        .textContent =
        sensorName(
            payload.sensor.sensor_type
        );

    document
        .getElementById("sensor-value")
        .textContent =
        payload.sensor.sensor_value +
        " " +
        payload.sensor.unit;

}


/*********************************************************************
 * Atualiza localização
 *********************************************************************/

function updateLocation(payload) {

    document
        .getElementById("node-name")
        .textContent =
        payload.node_name;

    document
        .getElementById("coordinates")
        .textContent =
        Number(payload.location.latitude).toFixed(4)
        + ", " +
        Number(payload.location.longitude).toFixed(4);

}


/*********************************************************************
 * Atualiza horário
 *********************************************************************/

function updateTimestamp(payload) {

    const date =
        new Date(payload.timestamp);

    document
        .getElementById("timestamp")
        .textContent =
        date.toLocaleString();

    document
        .getElementById("last-update")
        .textContent =
        "Last update: " +
        date.toLocaleString();

    document
        .getElementById("source")
        .textContent =
        "Source: " +
        sourceName(
            payload.source
        );

}


/*********************************************************************
 * Google Maps
 *********************************************************************/

function configureMapButton(payload) {

    const url =
        "https://www.google.com/maps?q="
        + payload.location.latitude
        + ","
        + payload.location.longitude;

    document
        .getElementById("map-button")
        .onclick = () =>
            window.open(`https://www.google.com/maps/search/?api=1&query=${payload.location.latitude},${payload.location.longitude}`,
    "_blank"
            );

}


/*********************************************************************
 * Offline
 *********************************************************************/

function showOffline() {

    updateStatus(false);

}


/*********************************************************************
 * Notificação
 *********************************************************************/

function showNotification(message) {

    const banner =
        document.getElementById("notification");

    document
        .getElementById("notification-text")
        .textContent =
        message;

    banner.classList.remove("hidden");

    banner.classList.add("show");

    setTimeout(() => {

        banner.classList.remove("show");

        banner.classList.add("hidden");

    }, 5000);

}


/*********************************************************************
 * Relógio
 *********************************************************************/

function updateClock() {

    document
        .getElementById("clock")
        .textContent =
        new Date().toLocaleTimeString();

}


/*********************************************************************
 * Animação
 *********************************************************************/

function animateCard() {

    const card =
        document.getElementById("status-card");

    card.classList.remove("highlight");

    void card.offsetWidth;

    card.classList.add("highlight");

}


/*********************************************************************
 * Helpers
 *********************************************************************/

function sensorName(type) {

    switch (type) {

        case "water_level":
            return "🌊 Water Level";

        case "rainfall":
            return "🌧 Rainfall";

        case "soil_moisture":
            return "🌱 Soil Moisture";

        default:
            return type;

    }

}


function sourceName(source) {

    switch (source) {

        case "simulation":
            return "Simulation";

        case "hardware":
            return "Real Sensor";

        case "csv":
            return "CSV Dataset";

        case "api":
            return "External API";

        default:
            return source;

    }

}