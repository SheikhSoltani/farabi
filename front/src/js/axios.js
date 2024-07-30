import axios from 'axios';
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Если cookie начинается с имени, то извлекаем значение
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrfToken = getCookie('csrftoken');
const axiosInstance = axios.create({
  baseURL: 'https://api.idealf.kz/',
  withCredentials: true, // Replace with your actual base URL
  headers: {
      'X-CSRFToken': csrfToken
    }
});

export default axiosInstance;