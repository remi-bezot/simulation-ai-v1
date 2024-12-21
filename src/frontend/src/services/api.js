const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:8000";

const defaultHeaders = {
  "Content-Type": "application/json",
  Accept: "application/json",
};

// Journalisation des appels API
const logApiCall = (method, endpoint, body = null) => {
  console.log(`[API] ${method} ${endpoint}`, body || "");
};

// Gestion des erreurs API
const handleErrors = async (response) => {
  if (!response.ok) {
    const errorDetails = await response.json().catch(() => null);
    const errorMessage =
      errorDetails?.message ||
      `Erreur HTTP ${response.status}: ${response.statusText}`;
    console.error(`[API Error] ${errorMessage}`);
    throw new Error(errorMessage);
  }
  return response;
};

// Timeout pour les appels fetch
const fetchWithTimeout = (url, options, timeout = 10000) => {
  const controller = new AbortController();
  const signal = controller.signal;
  const timer = setTimeout(() => controller.abort(), timeout);

  return fetch(url, { ...options, signal }).finally(() => clearTimeout(timer));
};

// Génération des URL avec paramètres
const buildUrlWithParams = (url, params) => {
  const query = new URLSearchParams(params).toString();
  return query ? `${url}?${query}` : url;
};

// Appels génériques
export const get = async (endpoint, params = {}) => {
  logApiCall("GET", endpoint, params);
  const url = buildUrlWithParams(`${backendUrl}${endpoint}`, params);
  const response = await fetchWithTimeout(url, {
    method: "GET",
    headers: defaultHeaders,
  });
  await handleErrors(response);
  return await response.json();
};

export const post = async (endpoint, body) => {
  logApiCall("POST", endpoint, body);
  const response = await fetchWithTimeout(`${backendUrl}${endpoint}`, {
    method: "POST",
    headers: defaultHeaders,
    body: JSON.stringify(body),
  });
  await handleErrors(response);
  return await response.json();
};

export const put = async (endpoint, body) => {
  logApiCall("PUT", endpoint, body);
  const response = await fetchWithTimeout(`${backendUrl}${endpoint}`, {
    method: "PUT",
    headers: defaultHeaders,
    body: JSON.stringify(body),
  });
  await handleErrors(response);
  return await response.json();
};

export const del = async (endpoint) => {
  logApiCall("DELETE", endpoint);
  const response = await fetchWithTimeout(`${backendUrl}${endpoint}`, {
    method: "DELETE",
    headers: defaultHeaders,
  });
  await handleErrors(response);
  return await response.json();
};

// Gestion des dimensions
export const addDimension = async (dimension) => {
  return await post("/api/multiverse", dimension);
};

export const deleteDimension = async (dimensionId) => {
  return await del(`/api/multiverse/${dimensionId}`);
};

export const updateDimension = async (dimensionId, updates) => {
  return await put(`/api/multiverse/${dimensionId}`, updates);
};

// Gestion des multivers
export const getMultiverses = async () => {
  return await get("/api/multiverse");
};

export const addMultiverse = async (multiverse) => {
  return await post("/api/multiverse", multiverse);
};

export const deleteMultiverse = async (multiverseId) => {
  return await del(`/api/multiverse/${multiverseId}`);
};

// Gestion des univers
export const getUniverses = async (multiverseId) => {
  return await get(`/api/universes/${multiverseId}`);
};

export const addUniverse = async (multiverseId, universe) => {
  return await post(`/api/universes/${multiverseId}`, universe);
};

export const deleteUniverse = async (universeId) => {
  return await del(`/api/universes/${universeId}`);
};
