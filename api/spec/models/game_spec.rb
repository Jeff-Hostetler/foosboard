require "rails_helper"

RSpec.describe Game do
  it "returns false when there is no active game" do
    expect(Game.in_progress?).to eq false
  end

  it "returns true when a game is in progress" do
    Game.create(
      team_1_score: 0,
      team_2_score: 0,
      in_progress: true,
      team_1_defense_id: 123,
      team_1_offense_id: 123,
      team_2_offense_id: 987,
      team_2_defense_id: 987
    )

    expect(Game.in_progress?).to eq true
  end
end
