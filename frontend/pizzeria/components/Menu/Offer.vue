<template>
  <v-container>
<!--    <h1>Jedálny lístok</h1>-->
    <v-row>
      <Pizza/>
    </v-row>
    <v-row>
      <Ingredient/>
    </v-row>
    <v-row>
      <Menu/>
    </v-row>
  </v-container>
</template>

<script>
import Pizza from "./Pizza";
import Ingredient from "./Ingredient";
import Menu from "./Menu";

export default {
  name: "Offer",
  components: {
    Pizza,
    Ingredient,
    Menu
  }
}
</script>

<style scoped>

</style>
