import axios from 'axios';

const axiosInstance = axios.create({
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: "X-CSRFTOKEN",
  baseURL: 'https://api.idealf.kz/',
  withCredentials: true,
});

export default axiosInstance;