<template>
  <v-container>
    <Offer />
  </v-container>
</template>

<script>
import Offer from "../components/Menu/Offer";

export default {
  name: 'ponuka',
  components: {
    Offer
  },
  methods: {
    fetchAllData() {
      this.$store.dispatch('fetchAllData')
    },
  },
  created() {
    if (this.$store.state.offer.loaded === false) {
      this.$store.dispatch('fetchAllData');
    }
  }
}
</script>

<style scoped>

</style>
