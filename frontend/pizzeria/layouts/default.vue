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

<style lang="scss">

//.theme--dark.v-application {
//  background-color: var(--v-background-base, #121212) ;
//}

.v-app {
  font-family: "FredericatheGreat", sans-serif !important;
  background: var(--v-background-base) !important;
  color: var(--v-secondary-base) !important;
  overflow-y: auto !important;
  margin-top: 8vh;
}
</style>
