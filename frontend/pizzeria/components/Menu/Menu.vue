<template>
  <v-container class="offer-box">
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
          <Offer/>
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
.offer-box {
  background: rgba(15, 15, 15, 0.7);
  opacity: 0.8;
  padding: 0 2% 2% 3%;
  border-radius: 20px;
}

.hover-row {
  padding-left: 2%;
  border-radius: 10px;

  &:hover {
    color: black;
    background: rgba(white, 0.4);
  }

}

.filter {
  display: inline;
}

</style>
