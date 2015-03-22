require "active_record"
require_relative "../../app/models/player"
require_relative "../../app/models/game"
require_relative "../../app/services/stats_service"

RSpec.describe StatsService do
  FakePlayer = Struct.new(:id, :nickname)

  let(:fake_player) { class_double(Player).as_stubbed_const }
  let(:fake_game) { class_double(Game).as_stubbed_const }
  let(:sample_player) { FakePlayer.new(id = 123, nickname = "Lazy Laser") }

  before do
    allow(fake_game).to receive(:win_percentage_for_player)
    allow(fake_game).to receive(:goals_scored_for_player)
    allow(fake_game).to receive(:goals_against_for_player)

    allow(fake_player).to receive(:all).and_return([sample_player])
  end

  it "returns an empty collection when there are no players" do
    allow(fake_player).to receive(:all).and_return([])

    expect(StatsService.new.all_stats).to eq []
  end

  it "returns all the player's nicknames" do
    allow(fake_player).to receive(:all).and_return([
      FakePlayer.new(id = 123, nickname = "Lazy Laser")
    ])

    all_stats = StatsService.new.all_stats

    expect(all_stats.first[:nickname]).to eq "Lazy Laser"
  end

  it "returns each player's win percentage" do
    allow(fake_game).to receive(:win_percentage_for_player).and_return(100)

    all_stats = StatsService.new.all_stats

    expect(fake_game).to have_received(:win_percentage_for_player).
      with(sample_player)
    expect(all_stats.first[:win_percentage]).to eq 100
  end

  it "calculates the goals a player scored" do
    allow(fake_game).to receive(:goals_scored_for_player).and_return(42)

    all_stats = StatsService.new.all_stats

    expect(fake_game).to have_received(:goals_scored_for_player).
      with(sample_player)
    expect(all_stats.first[:goals_scored]).to eq 42
  end

  it "caculates the goals scored against a player" do
    allow(fake_game).to receive(:goals_against_for_player).and_return(7)

    all_stats = StatsService.new.all_stats

    expect(fake_game).to have_received(:goals_against_for_player).
      with(sample_player)
    expect(all_stats.first[:goals_against]).to eq 7
  end
end
