import axios from "axios";

const API_URL = "http://192.168.55.56:8000/auth/";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const register = (userData) => {
  console.log("Registering user:", userData);
  return api.post("register", userData); // Return the promise
};

export const login = (userData) => {
  console.log("Logging in user:", userData);
  return api.post("login", userData);
};

export const logout = () => api.post("logout");
export const getUser = () => api.get("user");
