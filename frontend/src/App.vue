<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row mb-4">
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Tytuł"
          v-model="book.title"
        />
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Autor"
          v-model="book.author"
        />
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Strony"
          v-model="book.pages"
        />
        <button class="btn btn-success ml-3">Dodaj</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Tytuł</th>
        <th>Autor</th>
        <th>Strony</th>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id" @dblclick="$data.book = book">
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.pages }}</td>
          <td>
            <button
              class="btn btn-danger btn-sm mx-1"
              @click="deleteBook(book)"
            >
              X
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      books: [],
      book: {},
    };
  },
  async created() {
    await this.getBooks();
  },

  methods: {
    submitForm() {
      if (this.book.id === undefined) {
        this.addBook();
      } else {
        this.editBook();
      }
    },
    async getBooks() {
      var response = await fetch("http://127.0.0.1:8000/api/books/");
      this.books = await response.json();
    },
    async addBook() {
      await this.getBooks();
      await fetch("http://127.0.0.1:8000/api/books/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.book),
      });
      await this.getBooks();

      this.clear();
    },

    async editBook() {
      await this.getBooks();
      await fetch(`http://127.0.0.1:8000/api/books/${this.book.id}/`, {
        method: "put",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.book),
      });
      await this.getBooks();

      this.book = {};
      this.clear();
    },

    async deleteBook(book) {
      await this.getBooks();
      await fetch(`http://127.0.0.1:8000/api/books/${book.id}/`, {
        method: "delete",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.book),
      });
      await this.getBooks();
    },

    clear() {
      this.book.title = "";
      this.book.author = "";
      this.book.pages = "";
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
