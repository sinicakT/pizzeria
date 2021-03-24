import axios from 'axios'

export const state = () => ({
  offer: {
    loaded: false,
    pizzas: [],
    ingredients: [],
    menu: []
  }
});

export const mutations = {
  setPizzas(state:any, pizzas:any) {
    state.offer.pizzas = pizzas
  },
  setIngredients(state:any, ingredients:any) {
    state.offer.ingredients = ingredients
  },
  setMenu(state:any, menu:any) {
    state.offer.menu = menu
  },
  setCompleteOffer(state:any, data:any) {
    state.offer = {
      pizzas: data['pizzas'],
      ingredients: data['ingredients'],
      menu: data['menu']

    }
  }
};

export const actions = {
  // nuxtServerInit(vuexContext:any, context:any) {
  //   return axios.get('http://127.0.0.1:8000/api/pizza/')
  //     .then(res => {
  //       console.log(res);
  //       vuexContext.commit('setCompleteOffer', {
  //         'loaded': true,
  //         'pizzas': res.data,
  //         'ingredients': [],
  //         'menu': []
  //       });
  //     })
  //     .catch(e => context.error(e))
  // },
  fetchAllData(vuexContext: any) {
    return axios.get('http://127.0.0.1:8000/api/pizza/')
      .then(res => {
        vuexContext.commit('setCompleteOffer', {
          'loaded': true,
          'pizzas': res.data,
          'ingredients': [],
          'menu': []
        });
      })
      .catch(e => console.log(e))
  },
  setPizzas(vuexContext:any, pizzas:any) {
    vuexContext.commit('setPizzas', pizzas)
  },
  setIngredients(vuexContext:any, ingredients:any) {
    vuexContext.commit('setPizzas', ingredients)
  },
  setMenu(vuexContext:any, menu:any) {
    vuexContext.commit('setPizzas', menu)
  },
  setCompleteOffer(vuexContext:any, data:any) {
    vuexContext.commit('setCompleteOfferPizzas', data)
  }
}

export const getters = () => ({
  pizzas(state:any) {
    return state.offer.pizzas
  },
  ingredients(state:any) {
    return state.offer.ingredients
  },
  menu(state:any) {
    return state.offer.menu
  },
  completeOffer(state:any) {
    return state.offer
  }
})
