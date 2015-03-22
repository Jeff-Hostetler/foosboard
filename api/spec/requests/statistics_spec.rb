require "rails_helper"

RSpec.describe "Statistics API" do
  describe "GET /stats" do
    it "returns the statistics for all players" do
      seed_player_with_stats

      get "/stats"

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)
      player_1_stats = response_body[:stats].find do |s|
        s[:nickname] == "Lumpy Space Princess"
      end

      expect(player_1_stats[:win_percentage]).to eq 100
      expect(player_1_stats[:goals_scored]).to eq 5
      expect(player_1_stats[:goals_against]).to eq 2
    end
  end

  def seed_player_with_stats
    player_1 = Player.create(nickname: "Lumpy Space Princess")
    player_2 = Player.create(nickname: "Ice King")

    Game.create(
      team_1_score: 5,
      team_2_score: 2,
      in_progress: false,
      team_1_defense_id: player_1.id,
      team_1_offense_id: player_1.id,
      team_2_offense_id: player_2.id,
      team_2_defense_id: player_2.id
    )
  end
end
