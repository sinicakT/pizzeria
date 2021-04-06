<template>
  <v-container>
    <v-list rounded color="primary">
      <v-list-item v-for="(ingredient, index) in ingredients" :key="index">
        <v-btn block @click="changeList(ingredient.id)" :color=btnColor(ingredient.id)>
          {{ ingredient.name }}
        </v-btn>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
export default {
  name: "IngredientsFilter",
  data() {
    return {
      filterList: [] = []
    }
  },
  computed: {
    ingredients() {
      return this.$store.state.menu.ingredients_list
    },
  },
  methods: {
    btnColor(id) {
      return this.filterList.some(item => item === id) ? 'black' : 'background darken-2'
    },
    changeList(id) {
      const index = this.filterList.indexOf(id);
      if (index > -1) {
        this.filterList.splice(index, 1);
      } else {
        this.filterList.push(id)
      }
      this.$emit('listChanged', this.filterList);
    },
  }
}
</script>

<style lang="scss">

</style>
