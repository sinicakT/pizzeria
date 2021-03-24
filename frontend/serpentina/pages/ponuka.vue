<template>
  <div>
    <h1> Ponuka </h1>
    <v-btn color="black" @click="fetchAllData">Load data</v-btn>
  </div>
</template>

<script>
export default {
  name: 'ponuka',
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
