<template>
  <v-container class="align-left py-10">
    <h4 class="pb-4">Prílohy</h4>
    <v-row v-for="cattegory in Object.keys(ingredients)" :key="cattegory">
      <v-col cols="6" md="8" class="py-0 text-caption">
        {{ ingredients[cattegory] }}
      </v-col>
      <v-col cols="6" md="4" class="py-0 text-caption">
        <v-col cols="7" md="6" class="pa-0"> </v-col>
        <v-col cols="5" md="6" class="pa-0">
          <span>{{ cattegory }} €</span>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Ingredient",
  computed: {
    ingredients() {
      return this.$store.state.menu.ingredients
    }
  }
}
</script>

<style scoped>

</style>
