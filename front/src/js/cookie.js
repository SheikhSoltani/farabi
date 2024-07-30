
    export function getConfig(t) {
     const config = {
        headers: {
        'Content-Type': t,
        'Access-Control-Allow-Origin': '*',
        }
    };
    return config;
}