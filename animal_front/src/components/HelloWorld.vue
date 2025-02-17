<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="(animal, index) in animals" :key="index" style="display:block">
        {{index}}-{{animal.name}}-{{animal.author}}
      </li>
    </ul>
    <!-- form to add a book -->
    <form action="">
      输入书名：<input type="text" placeholder="animal name" v-model="inputAnimal.name"><br>
      输入作者：<input type="text" placeholder="book author" v-model="inputAnimal.author"><br>
    </form>
    <button type="submit" @click="animalSubmit()">submit</button>
  </div>
</template>

<script>
import {getAnimals, postAnimal} from '../api/api.js'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      animals: [
        {name: 'test', author: 't'},
        {name: 'test2', author: 't2'}
      ],
      // book data in the form
      inputAnimal: {
        "name": "",
        "author": "",
      }
    }
  },
  methods: {
    loadAnimals () {
      getAnimals().then(response => {
        this.animals = response.data
      })
    }, // load books list when visit the page
    animalSubmit () {
      postAnimal(this.inputAnimal.name, this.inputAnimal.author).then(response => {
        console.log(response)
        this.loadAnimals()
      })
    } // add a book to backend when click the button
  },
  created: function () {
    this.loadAnimals()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
