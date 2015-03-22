class StatusesController < ApplicationController
  def show
    status = Game.in_progress? ? "in progress" : "open"

    render json: {status: status}
  end
end
