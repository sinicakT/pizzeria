import axios from 'axios'

export const state = () => ({
  menu: {
    loaded: false,
    pizzas: [],
    ingredients: [],
    ingredients_list: [],
    offer: []
  },
  galleries: []
});

export const mutations = {
  setPizzas(state:any, pizzas:any) {
    state.menu.pizzas = pizzas
  },
  setIngredients(state:any, ingredients:any) {
    state.offer.ingredients = ingredients
  },
  setOffer(state:any, menu:any) {
    state.menu.offer = menu
  },
  setCompleteMenu(state:any, data:any) {
    state.menu = {
      pizzas: data['pizzas'],
      ingredients: data['ingredients'],
      ingredients_list: data['ingredients_list'],
      offer: data['offer']

    }
  },
  setGalleries(state: any, data: any) {
    var gallery_index = 0
    data.forEach((gallery: any) => {
      gallery.images.forEach((image: any) => {
        image.gallery_index = gallery_index
        gallery_index++
      })
    })
    state.galleries = data

  }
};

export const actions = {
  fetchAllData(vuexContext: any) {
    return axios.get(process.env.baseUrl + '/api/menu/')
      .then(res => {
        const pizzas: any[] = [];
        res.data.pizza.forEach((pizza: any) => {
          const ingredients_array: string[] = [];
          pizza.ingredients.forEach((ingredient: any) => {
            ingredients_array.push(ingredient.name)
          })
          pizzas.push({
            ...pizza,
            'ingredients_arr': ingredients_array
          })
        })
        vuexContext.commit('setCompleteMenu', {
          'loaded': true,
          'pizzas': pizzas,
          'ingredients': res.data.ingredients,
          'ingredients_list': res.data.ingredients_list,
          'offer': res.data.offer
        });
      })
      .catch(e => console.log(e))
  },

  fetchGalleries(vuexContext:any) {
    return axios.get(process.env.baseUrl + '/api/gallery/')
      .then(res => {
        vuexContext.commit('setGalleries', res.data);
      })
      .catch(e => console.log(e))
  },

  setPizzas(vuexContext:any, pizzas:any) {
    vuexContext.commit('setPizzas', pizzas)
  },
  setIngredients(vuexContext:any, ingredients:any) {
    vuexContext.commit('setPizzas', ingredients)
  },
  setOffer(vuexContext:any, menu:any) {
    vuexContext.commit('setPizzas', menu)
  },
  setCompleteMenu(vuexContext:any, data:any) {
    vuexContext.commit('setCompleteMenu', data)
  }
}

export const getters = () => ({
  pizzas(state:any) {
    return state.menu.pizzas
  },
  ingredients(state:any) {
    return state.offer.ingredients
  },
  offer(state:any) {
    return state.menu.offer
  },
  menu(state:any) {
    return state.menu
  },
  galleries(state:any) {
    return state.galleries
  }
})
