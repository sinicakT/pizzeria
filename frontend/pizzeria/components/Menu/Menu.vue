<template>
  <v-container class="offer-box">
    <!--    <h1>Jedálny lístok</h1>-->
    <v-row>
      <v-col cols="12">
        <v-row>
          <Pizza/>
        </v-row>
        <v-row>
          <Ingredient/>
        </v-row>
        <v-row>
          <Offer/>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Pizza from "./Pizza";
import Ingredient from "./Ingredient";
import Offer from "./Offer";

export default {
  name: "Menu",
  components: {
    Pizza,
    Ingredient,
    Offer
  },
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
