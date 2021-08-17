<template>
  <v-app dark>
    <Header />
    <v-main class="main-container">
      <v-container col="12">
        <div class="background" />
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Header from '~/components/Header'
import Footer from '~/components/Footer'

export default {
  components: {
    Header,
  },
}
</script>

<style lang="scss">

//.theme--dark.v-application {
//  background-color: var(--v-background-base, #121212) ;
//}

.v-app {
  font-family: "FredericatheGreat", sans-serif !important;
  color: var(--v-secondary-base) !important;
  overflow-y: auto !important;
  margin-top: 8vh;
}
</style>
