<template>
  <div>
    <vue-masonry-wall class="gallery" :items="gallery" :options="{width: 150, padding: { default: 12, 1: 6, 2: 8}}">
      <template v-slot:default="{item}">
        <v-img contain :src="item.url" alt="" class="gallery-image" max-width="300" justify="space-around"/>
      </template>
    </vue-masonry-wall>
  </div>
</template>

<script>
import VueMasonryWall from 'vue-masonry-wall'

export default {
  name: 'galeria',
  components: {
    VueMasonryWall
  },
  computed: {
    gallery() {
      return this.$store.state.gallery
    }
  },
  created() {
    if (this.$store.state.gallery.length < 1) {
      this.$store.dispatch('fetchGallery');
    }
  }
}
</script>

<style lang="scss">
  .gallery {
    flex-flow: row wrap;
    width: 100%;
    .masonry-column {
      flex: auto;
      min-width: 300px;
      margin: 0 8px 8px 0;
      .masonry-item {
        width: 100%;
        align-items: stretch;
        justify-content: center;
      }
    }
  }
</style>
