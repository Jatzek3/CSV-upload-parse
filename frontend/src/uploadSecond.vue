<template>
  <form @submit.prevent="sendFile" enctype="multipart/form-data" class="form">
    <label for="file" class="label">Upload file with client requests</label>
    <input type="file" ref="file" @change="selectFile" />
    <button>Send</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "UploadSecond",
  data() {
    return {
      file: "",
    };
  },
  methods: {
    selectFile() {
      this.file = this.$refs.file.files[0];
    },
    async sendFile() {
      const formData = new FormData();
      formData.append("file", this.file);
      try {
        await axios.post("http://127.0.0.1:5000/uploadTwo", formData);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
</style>
