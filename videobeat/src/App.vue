<template>
  <div class="app">
    <header-comp />
    <upload />
    <upload-second />
    <compute />
  </div>
</template>

<script>
import Upload from "./Upload";
import HeaderComp from "./HeaderComp";
import UploadSecond from "./uploadSecond";
import Compute from "./Compute";

export default {
  name: "App",
  components: { Upload, HeaderComp, UploadSecond, Compute },
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
