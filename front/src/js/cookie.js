function getCookie(name) {
  let cookieValue = null;
  console.log('CALLED COOKIE GETTER  ' + document.cookie + "doc " + document)
  if (document.cookie && document.cookie !== '') {
      console.log('IN FIRST IF')
    const cookies = document.cookie.split(';');
      console.log(cookies)
    for (let i = 0; i < cookies.length; i++) {
        console.log(cookies)
      const cookie = cookies[i].trim();
      // Если cookie начинается с имени, то извлекаем значение
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
          console.log(cookieValue)
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
    export function getConfig(t) {
    console.log(getCookie('csrftoken'), "WQEWEEWQ")
        return {
        headers: {
            'Content-Type': t,
            'Access-Control-Allow-Origin': '*',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };
}