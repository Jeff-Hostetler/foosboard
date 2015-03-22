require "rails_helper"

RSpec.describe "Status API" do
  describe "GET /status" do
    it "returns an 'in progress' status when the table is being used" do
      Game.create(
        team_1_score: 0,
        team_2_score: 0,
        in_progress: true,
        team_1_defense_id: 123,
        team_1_offense_id: 123,
        team_2_offense_id: 987,
        team_2_defense_id: 987
      )

      get "/status", query = {}, {"Accept" => "application/json"}

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body[:status]).to eq "in progress"
    end

    it "returns an 'open' status when the table is available" do
      get "/status", query = {}, {"Accept" => "application/json"}

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body[:status]).to eq "open"
    end
  end
end
