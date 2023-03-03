import axios from "axios"

export const api = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/"
});


export const getPosts = async () => {
    const response = await api.get('/posts')
    return response.data
}


export const fastapi = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getData = async () => {
    const response = await fastapi.get("/search_pharmacies?");
    return response
}
