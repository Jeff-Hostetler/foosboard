class StatsController < ApplicationController
  def index
    render json: {stats: StatsService.new.all_stats}
  end
end
