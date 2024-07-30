import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://api.idealf.kz/',
  withCredentials: true,
});

export default axiosInstance;