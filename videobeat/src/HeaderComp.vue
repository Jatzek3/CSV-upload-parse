<template>
  <header>
    <h1>VideoBeat Vue-Flask App</h1>
    <p>
      Even though Vue 3 has stable release i decided to work with Vue 2, becouse
      the main project is using Vue 2.
    </p>
    <p>
      Flask was quite obvious choice for backend since creating rest API with
      flask is very easy. Flask is also very compact comparing to full featur
      framework like Django. Such a small project dont require using such a
      complex tool + DRF. There was also other framework which I considered
      aspecially FastAPI which i was recently very intrested, but its relatively
      new framework and I wasn't sure if I will be able find quickly apropriate
      learning materials/tutorials.
    </p>
  </header>
</template>

<script>
export default {
  name: "HeaderComp",
};
</script>

<style>
h1 {
  font-size: 2.5em;
  padding-left: 1em;
}
</style>