import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://api.idealf.kz/', // Replace with your actual base URL
});

export default axiosInstance;