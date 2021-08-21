<template>
  <v-container class="align-center">
    <v-row>
      <v-col col="12" md="10">
        <h1 class="text-center">Pizze</h1>
        <div v-if="pizzas.length < 1">
          Ľutujeme, taká pizza neexistuje. Skúste upraviť filter.
        </div>
        <v-row v-for="pizza in pizzas" :key="pizza.id" class="py-4 hover-row">
          <v-col cols="6" md="7">
            <v-row class="text-subheading font-weight-bold">
              <span>{{ pizza.number }}. {{ pizza.name }}</span>
            </v-row>
            <v-row class="text-caption text-lowercase font-weight-bold">
              <span v-for="(ingredient, index) in pizza.ingredients_arr" :key="pizza.id + '.' + ingredient">
                <span v-if="index > 0">, </span>
                  {{ ingredient }}
              </span>
            </v-row>
            <v-row class="text-caption font-weight-bold">
              <span>(
                <span v-for="(allergen, index) in pizza.allergens" :key="pizza.id + '.allergen' + allergen.number">
                   <span v-if="index > 0">, </span>
                  {{ allergen.number }}
                </span>
                )
              </span>
            </v-row>
          </v-col>
          <v-col cols="6" md="5" class="py-0 text-caption font-weight-bold price-box">
            <v-row v-for="size in pizza.size_values" :key="pizza.id + '.' + size.name">
              <v-col cols="7" md="6" class="pa-0">
                <span>{{ size.name }} {{ size.weight }}g</span>
              </v-col>
              <v-col cols="5" md="6" class="pa-0">
                <span>{{ size.price }} €</span>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="2" class="filter">
        <IngredientsFilter @listChanged="onListChangedHandler"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import IngredientsFilter from "@/components/Menu/IngredientsFilter";

export default {
  name: "Pizza",
  components: {
    IngredientsFilter,
  },
  data() {
    return {
      filterList: [] = []
    }
  },
  methods: {
    onListChangedHandler(filter) {
      this.filterList = filter
    },
  },
  computed: {
    pizzas() {
      const fullOffer = this.$store.state.menu.pizzas
      if (this.filterList.length < 1) {
        return fullOffer
      } else {
        const filteredOffer = []
        fullOffer.forEach((pizza) => {
          if (this.filterList.every(filter => pizza.ingredients.some(ingredient => ingredient.id === filter))) {
            filteredOffer.push(pizza)
          }
        })
        return filteredOffer
      }
    }
  }
  // computed: {
  //   pizzas() {
  //     return this.$store.state.menu.pizzas
  //   }
  // }
}
</script>

<style scoped lang="scss">
.price-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
