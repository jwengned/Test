import axiosInstance from './index'

const axios = axiosInstance

export const getAnimals = () => {return axios.get(`http://localhost:8000/api/animals/`)}

export const postAnimal = (animalName, animalAuthor) => {return axios.post(`http://localhost:8000/api/animals/`, {'name': animalName, 'author': animalAuthor})}