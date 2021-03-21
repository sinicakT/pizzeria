<template>
  <v-app dark>
    <Header />
    <v-main class="main-container">
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

  </v-app>
</template>

<script>
import Header from '~/components/Header'

export default {
  components: {
    Header
  },
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>

<style scoped>
@import "assets/scss/variables.scss";

.main-container {
  color: var(--v-secondary-base);
  overflow-y: auto !important;
  margin-top: 8vh;
}
</style>
