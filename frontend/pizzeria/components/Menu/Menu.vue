<template>
  <v-container>
    <!--    <h1>Jedálny lístok</h1>-->
    <v-row>
      <v-col cols="10">
        <v-row>
          <Pizza :pizzas="sortedPizzas"/>
        </v-row>
        <v-row>
          <Ingredient/>
        </v-row>
        <v-row>
          <Offer />
        </v-row>
      </v-col>
      <v-col cols="2" class="filter">
        <IngredientsFilter @listChanged="onListChangedHandler"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import IngredientsFilter from "./IngredientsFilter";
import Pizza from "./Pizza";
import Ingredient from "./Ingredient";
import Offer from "./Offer";

export default {
  name: "Menu",
  components: {
    IngredientsFilter,
    Pizza,
    Ingredient,
    Offer
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
    sortedPizzas() {
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
}
</script>

<style lang="scss">
.filter {
  display: inline;
}

</style>
