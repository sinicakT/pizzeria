<template>
  <v-container class="align-center">
    <h1>Pizze</h1>
    <v-row v-for="pizza in pizzas" :key="pizza.id" class="py-4">
      <v-col cols="6" md="8">
        <v-row class="font-weight-bold">
          <span>{{pizza.name}}</span>
        </v-row>
        <v-row class="text-body-2 text-lowercase">
          <span v-for="(ingredient, index) in pizza.ingredients_arr" :key="pizza.id + '.' + ingredient">
            <span v-if="index > 0">, </span>
            {{ ingredient }}
          </span>
        </v-row>
        <v-row class="text-caption">
            <span>(
              <span v-for="(allergen, index) in pizza.allergens" :key="pizza.id + '.allergen' + allergen.number">
                 <span v-if="index > 0">, </span>
                {{ allergen.number }}
              </span>
              )
            </span>
        </v-row>
      </v-col>
      <v-col cols="6" md="4" class="py-0 text-caption">
        <v-row v-for="size in pizza.size_values" :key="pizza.id + '.' + size.name">
          <v-col cols="7" md="6" class="pa-0">
            <span>{{size.name}} {{size.weight}}g</span>
          </v-col>
          <v-col cols="5" md="6" class="pa-0">
            <span>{{size.price}} €</span>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Pizza",
  computed: {
    pizzas() {
      return this.$store.state.offer.pizzas
    }
  }
}
</script>

<style scoped>

</style>
