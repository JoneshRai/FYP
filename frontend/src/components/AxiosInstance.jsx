import axios from 'axios';

const baseUrl = 'http://127.0.0.1:8000/';

const AxiosInstance = axios.create({
  baseURL: baseUrl,
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

AxiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('Token');

    if (token) {
      config.headers.Authorization = `Token ${token}`; // Use backticks for template literals
    } else {
      config.headers.Authorization = '';
    }
    return config;
  },
  
);

AxiosInstance.interceptors.response.use(

    (response) => {
      // Return the response if it's successful
      return response;
    },
    (error) => {
      // Check if the error is due to unauthorized access (401)
      if (error.response && error.response.status === 401) {
        
        localStorage.removeItem('Token');
        
        window.location.href = '/';
      }
    }
  
  
)

export default AxiosInstance;
