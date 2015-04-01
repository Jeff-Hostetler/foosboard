class StatusesController < ApplicationController
  def show
    game = Game.last
    status = if game && game.in_progress?
               "in progress"
             else
               "open"
             end

    render json: {status: status}
  end
end
