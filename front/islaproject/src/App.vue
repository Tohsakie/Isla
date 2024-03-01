<script setup>
import MainSection from './components/MainSection.vue'
import ProductVue from './components/ProductVue.vue'
document.body.classList.add("dark");
</script>


<template>

  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <MainPage msg="You did it!" />
    </div>
  </header> -->



    <div id="back-colors" class="relative flex flex-col h-[100vh] items-center justify-center bg-white dark:bg-black transition-bg">
        <div class="absolute inset-0 overflow-hidden">
            <div class="jumbo absolute -inset-[10px] opacity-50"></div>
        </div>
    </div>

    <div id="back-bg">
      <MainSection />
    </div>


  


</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

</style>
