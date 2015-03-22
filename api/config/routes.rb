Rails.application.routes.draw do
  resources :games, only: [:index, :create, :update]
  resources :players, only: [:index]
end
