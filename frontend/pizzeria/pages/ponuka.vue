<template>
  <v-container>
    <Menu />
  </v-container>
</template>

<script>
import Menu from "../components/Menu/Menu";

export default {
  name: 'ponuka',
  components: {
    Menu
  },
  methods: {
    fetchAllData() {
      this.$store.dispatch('fetchAllData')
    },
  },
  created() {
    if (this.$store.state.menu.loaded === false) {
      this.$store.dispatch('fetchAllData');
    }
  }
}
</script>

<style scoped>

</style>
