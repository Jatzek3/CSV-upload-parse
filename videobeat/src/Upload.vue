<template>
  <form @submit.prevent="sendFile" enctype="multipart/form-data" class="form">
    <label for="file" class="label">Upload file with ad blocks</label>
    <input type="file" ref="file" @change="selectFile" />
    <button>Send</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "Upload",
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
        await axios.post("http://localhost:5000/uploadOne", formData);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
</style>
