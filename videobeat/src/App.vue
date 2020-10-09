<template>
  <div class="app">
    <header-comp />
    <upload />
    <upload-second />
  </div>
</template>

<script>
import Upload from "./Upload.vue";
import HeaderComp from "./HeaderComp.vue";
import UploadSecond from "./uploadSecond";

export default { 
  
  name: "App",
  components: { Upload, HeaderComp, UploadSecond },
};
</script>

<style>
.app {
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5em;
}
</style>
