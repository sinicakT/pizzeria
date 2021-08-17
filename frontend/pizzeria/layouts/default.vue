<template>
  <v-app dark>
    <Header />
    <v-main class="main-container">
      <v-container col="12">
        <div class="background" />
        <nuxt />
      </v-container>
    </v-main>
    <Footer />

  </v-app>
</template>

<script>
import Header from '~/components/Header'
import Footer from '~/components/Footer'

export default {
  components: {
    Header,
    Footer
  },
}
</script>

<style lang="scss">
</style>
