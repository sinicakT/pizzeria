<template>
  <div>
    <ModalGalleryDetail :index="index" v-model="showDetail"/>
    <vue-masonry-wall class="gallery mx-auto" :items="gallery" :options="{width: 150, padding: { default: 12, 1: 6, 2: 8}}">
      <template v-slot:default="{item}">
        <v-img contain :src="item.preview_url" class="gallery-image" justify="space-around" @click="imageClickHandler(item.index)"/>
      </template>
    </vue-masonry-wall>
  </div>
</template>

<script>
import VueMasonryWall from 'vue-masonry-wall'
import ModalGalleryDetail from "../components/GalleryDetail";

export default {
  name: 'galeria',
  components: {
    ModalGalleryDetail,
    VueMasonryWall,
  },
  data() {
    return {
      showDetail: false,
      index: 0
    }
  },
  computed: {
    gallery() {
      return this.$store.state.gallery
    }
  },
  methods: {
    imageClickHandler(index) {
      // event.preventDefault();
      this.index = +index;
      this.showDetail = true;
    },
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
        justify-content: stretch;
      }
    }
  }
</style>
