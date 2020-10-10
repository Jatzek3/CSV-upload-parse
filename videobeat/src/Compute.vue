<template>
  <div>
    <button @click="compute">Send</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Compute",
  data() {
    return {
      blocks: [],
    };
  },
  methods: {
    async compute() {
      try {
        await axios.get("http://localhost:5000/compute").then((resp) => {
          console.log(resp.data);
          this.blocks.push(resp.data);
        });
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
</style>