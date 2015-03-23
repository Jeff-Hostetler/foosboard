class GamesController < ApplicationController
  def index
    render json: Game.includes(:team_1_defense,
                               :team_1_offense,
                               :team_2_defense,
                               :team_2_offense)
  end

  def show
    render json: Game.find(params[:id])
  end

  def create
    render json: Game.create(game_params.merge(in_progress: true)),
      status: :created
  end

  def update
    game = Game.find(params[:id])

    game.update_attributes(game_update_params.merge(in_progress: false))

    render json: game, status: :ok
  end

  private

  def game_params
    {
      team_1_defense_id: params[:team_1][:defense][:id],
      team_1_offense_id: params[:team_1][:offense][:id],
      team_2_offense_id: params[:team_2][:offense][:id],
      team_2_defense_id: params[:team_2][:defense][:id],
    }
  end

  def game_update_params
    params.permit(:team_1_score,
                  :team_2_score)
  end
end
