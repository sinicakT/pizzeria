import axios from 'axios'

export const state = () => ({
  offer: {
    loaded: false,
    pizzas: [],
    ingredients: [],
    ingredients_list: [],
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
  setmenu(state:any, menu:any) {
    state.offer.menu = menu
  },
  setCompleteOffer(state:any, data:any) {
    state.offer = {
      pizzas: data['pizzas'],
      ingredients: data['ingredients'],
      ingredients_list: data['ingredients_list'],
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
    return axios.get('http://127.0.0.1:8000/api/menu/')
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
        vuexContext.commit('setCompleteOffer', {
          'loaded': true,
          'pizzas': pizzas,
          'ingredients': [],
          'ingredients_list': res.data.ingredients_list,
          'menu': res.data.menu
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
  setmenu(vuexContext:any, menu:any) {
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
