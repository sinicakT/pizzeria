<template>
  <v-container class="align-center">
    <v-row v-for="category in offer" :key="offer.id" class="align-center" >
      <h3 class="mx-auto">{{ category.name }}</h3>
      <v-col cols="12">
        <v-row v-for="(item, index) in category.offer_item" :key="offer.id + '.' + index">
          <v-col cols="6" md="8">
            <v-row class="font-weight-bold text-caption">
              <span>{{ item.name }}</span>
            </v-row>
            <v-row class="text-body-2 text-caption">
              <span> {{ item.description }} </span>
            </v-row>
          </v-col>
          <v-col cols="6" md="4" class="py-0 text-caption">
            <v-col cols="7" md="6" class="pa-0">
              <span>{{ item.capacity }}</span>
            </v-col>
            <v-col cols="5" md="6" class="pa-0">
              <span>{{ item.price }} €</span>
            </v-col>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Offer",
  // data() {
  //   return {
  //     offer: [] = []
  //   }
  // },
  computed: {
    offer() {
      return this.$store.state.menu.offer
    }
  }
}
</script>
