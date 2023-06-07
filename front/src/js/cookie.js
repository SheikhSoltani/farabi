function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    }
    export function getConfig(t) {
     const config = {
        headers: {
        'Content-Type': t,
        'Access-Control-Allow-Origin': '*',
        'X-CSRFTOKEN': getCookie('csrftoken')
        }
    };
    return config;
}